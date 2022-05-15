import typer


def greet() -> None:
    """Welcome to our awesome CLI app!"""
    typer.echo("Hello, World!")


if __name__ == "__main__":
    typer.run(greet)
