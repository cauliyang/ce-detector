"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Ce Detector."""


if __name__ == "__main__":
    main(prog_name="ce-detector")  # pragma: no cover
