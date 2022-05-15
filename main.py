import typer


def greet(name: str = typer.Option(..., prompt=True)) -> None:
    """Welcome to our awesome CLI app!
    
    Pass in a name either by using the option, or the prompt."""
    bolded = typer.style(name, bold=True)
    typer.secho(f"Hello, {bolded}!", fg=typer.colors.GREEN)


if __name__ == "__main__":
    typer.run(greet())
