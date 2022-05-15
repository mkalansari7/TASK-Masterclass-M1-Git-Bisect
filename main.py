import typer


def greet(name: str) -> None:
    """Welcome to our awesome CLI app!"""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    typer.run(greet)
