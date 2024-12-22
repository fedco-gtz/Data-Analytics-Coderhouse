import re

# Ruta al archivo README
readme_path = "README.md"

# Expresión regular para encontrar tareas completadas
task_pattern = r"- \[(x| )\]"

def update_progress():
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    # Contar las tareas y las completadas
    total_tasks = 0
    completed_tasks = 0

    for line in content:
        match = re.search(task_pattern, line)
        if match:
            total_tasks += 1
            if match.group(1) == "x":
                completed_tasks += 1

    # Calcular el progreso
    progress = int((completed_tasks / total_tasks) * 100) if total_tasks else 0

    # Actualizar la insignia de progreso
    progress_badge_pattern = r"!\[Progreso\]\(https://img\.shields\.io/badge/Progreso-\d+%25-brightgreen\.svg\)"
    new_badge = f"![Progreso](https://img.shields.io/badge/Progreso-{progress}%25-brightgreen.svg)"
    content = [
        re.sub(progress_badge_pattern, new_badge, line) if "Progreso" in line else line
        for line in content
    ]

    # Guardar el README actualizado
    with open(readme_path, "w", encoding="utf-8") as file:
        file.writelines(content)

    print(f"Progreso actualizado: {progress}%")

if __name__ == "__main__":
    update_progress()
