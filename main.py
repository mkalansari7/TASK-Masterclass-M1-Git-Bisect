import typer


def greet(name: str = typer.Option(..., prompt=True)) -> None:
    """Welcome to our awesome CLI app!"""
    typer.secho(f"Hello, {name}!", fg=typer.colors.GREEN)


if __name__ == "__main__":
    typer.run(greet())
