import typer


def greet() -> None:
    typer.echo("Hello, World!")


if __name__ == "__main__":
    typer.run(greet)
