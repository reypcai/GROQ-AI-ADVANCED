from rich.console import Console
from app.groq_client import generate_response

console = Console()

def run_cli():
    console.print("[bold green]Groq AI Advanced CLI[/bold green]")

    while True:
        prompt = console.input("[bold blue]You:[/bold blue] ")

        if prompt.lower() in ["exit", "quit"]:
            break

        response = generate_response(prompt)
        console.print(f"[bold yellow]AI:[/bold yellow] {response}\n")

if __name__ == "__main__":
    run_cli()