from pathlib import Path


JOKE = "My AI coding agent said it fixed the bug. It had only renamed it to ‘feature’ and updated the README."


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("The joke must be between 1 and 280 characters.")

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
