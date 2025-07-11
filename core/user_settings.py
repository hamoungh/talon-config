import csv
from pathlib import Path
from typing import IO, Callable

from talon import resource

# NOTE: This method requires this module to be one folder below the top-level
#   community folder.
SETTINGS_DIR = Path(__file__).parents[1] / "settings"
SETTINGS_DIR.mkdir(exist_ok=True)
PRIVATE_DIR = Path(__file__).parents[1] / "private"
PRIVATE_DIR.mkdir(exist_ok=True)

CallbackT = Callable[[dict[str, str]], None]
DecoratorT = Callable[[CallbackT], CallbackT]


def read_csv_list(
    f: IO, headers: tuple[str, str], is_spoken_form_first: bool = False
) -> dict[str, str]:
    rows = list(csv.reader(f))

    # print(str(rows))
    mapping = {}
    if len(rows) >= 2:
        actual_headers = rows[0]
        if not actual_headers == list(headers):
            print(
                f'"{f.name}": Malformed headers - {actual_headers}.'
                + f" Should be {list(headers)}. Ignoring row."
            )
        for row in rows[1:]:
            if len(row) == 0:
                # Windows newlines are sometimes read as empty rows. :champagne:
                continue
            if len(row) == 1:
                output = spoken_form = row[0]
            else:
                if is_spoken_form_first:
                    spoken_form, output = row[:2]
                else:
                    output, spoken_form = row[:2]

                if len(row) > 2:
                    print(
                        f'"{f.name}": More than two values in row: {row}.'
                        + " Ignoring the extras."
                    )
            # Leading/trailing whitespace in spoken form can prevent recognition.
            spoken_form = spoken_form.strip()
            mapping[spoken_form] = output

    return mapping


def write_csv_defaults(
    path: Path,
    headers: tuple[str, str],
    default: dict[str, str] = None,
    is_spoken_form_first: bool = False,
) -> None:
    if not path.is_file() and default is not None:
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for key, value in default.items():
                if key == value:
                    writer.writerow([key])
                elif is_spoken_form_first:
                    writer.writerow([key, value])
                else:
                    writer.writerow([value, key])


def track_csv_list(
    filename: str,
    headers: tuple[str, str],
    default: dict[str, str] = None,
    is_spoken_form_first: bool = False,
    private: bool = False,
) -> DecoratorT:
    assert filename.endswith(".csv")
    path = (PRIVATE_DIR / filename) if private else (SETTINGS_DIR / filename)
    write_csv_defaults(path, headers, default, is_spoken_form_first)

    def decorator(fn: CallbackT) -> CallbackT:
        """Register a callback that is triggered whenever *filename* changes.

        We use the Path instance directly (rather than its string representation)
        because ``resource.watch`` expects either a Path or a glob pattern.  In
        addition, we must return the *on_update* function so that Talon keeps a
        reference to it; otherwise the watcher can be garbage-collected and the
        decorator silently ends up returning *None*, which breaks imports that
        rely on the decorated function later in the module.
        """

        @resource.watch(path)
        def on_update(f):  # noqa: N802 – talon passes the open file object here
            data = read_csv_list(f, headers, is_spoken_form_first)
            fn(data)

        # Expose the watcher so that callers can keep a reference if they want
        # to (mirrors behaviour of track_file).
        return on_update

    return decorator


def append_to_csv(filename: str, rows: dict[str, str], private: bool = False):
    path = (PRIVATE_DIR / filename) if private else (SETTINGS_DIR / filename)
    assert filename.endswith(".csv")

    with open(str(path)) as file:
        line = None
        for line in file:
            pass
        needs_newline = line is not None and not line.endswith("\n")
    with open(path, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if needs_newline:
            writer.writerow([])
        for key, value in rows.items():
            writer.writerow([key] if key == value else [value, key])


WatchCallbackType = Callable[[IO], None]
WatchDecoratorType = Callable[[WatchCallbackType], WatchCallbackType]


def track_file(
    filename: str,
    default: str = "",
    private: bool = False,
) -> WatchDecoratorType:
    path = (PRIVATE_DIR / filename) if private else (SETTINGS_DIR / filename)
    if not path.is_file():
        path.write_text(default)

    def decorator(fn: WatchCallbackType) -> WatchCallbackType:
        @resource.watch(path)
        def on_update(f):
            fn(f)

        return on_update

    return decorator
