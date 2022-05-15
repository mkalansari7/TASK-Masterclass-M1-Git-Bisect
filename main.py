import typer


def greet(name: str = typer.Option(..., prompt=True)) -> None:
    """Welcome to our awesome CLI app!"""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    typer.run(greet())
