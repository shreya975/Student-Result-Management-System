import os

structure = {
    "EduTrack-Student-Result-Management-System": {
        "root_files": [
            "README.md"
        ],
        "docs": [
            "project_overview.md",
            "system_workflow.md",
            "user_roles.md",
            "data_design.md",
            "grading_logic.md",
            "analytics_design.md",
            "future_scope.md"
        ],
        "design": [
            "ui_guidelines.md",
            "color_typography.md"
        ],
        "data_models": [
            "users_schema.json",
            "students_schema.json",
            "subjects_schema.json"
        ],
        "planning": [
            "phase_plan.md",
            "timeline.md",
            "risks_and_assumptions.md"
        ],
        "implementation": [
            "README.md"
        ]
    }
}

def create_structure(base_path="."):
    project_name = list(structure.keys())[0]
    project = structure[project_name]

    root_path = os.path.join(base_path, project_name)
    os.makedirs(root_path, exist_ok=True)

    # Create root files
    for file in project["root_files"]:
        open(os.path.join(root_path, file), "w").close()

    # Create folders and files
    for folder, files in project.items():
        if folder == "root_files":
            continue
        folder_path = os.path.join(root_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for f in files:
            open(os.path.join(folder_path, f), "w").close()

    print("🎉 Project structure created successfully!")


if __name__ == "__main__":
    create_structure()
