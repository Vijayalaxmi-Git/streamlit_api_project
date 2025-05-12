import os


def create_streamlit_minimal_structure():
    """
    Creates only the missing parts of a Streamlit project structure:
    - .streamlit/secrets.toml (if missing)
    - Updates/creates .gitignore (if needed)
    - utils.py with just a comment
    - Does NOT modify main.py
    """
    print("Setting up missing Streamlit project components...")

    # 1. Create .streamlit folder if it doesn't exist
    if not os.path.exists(".streamlit"):
        os.makedirs(".streamlit")
        print("Created .streamlit directory")
    else:
        print(".streamlit directory already exists")

    # 2. Create secrets.toml with API_KEY placeholder if it doesn't exist
    secrets_path = os.path.join(".streamlit", "secrets.toml")
    if not os.path.exists(secrets_path):
        with open(secrets_path, "w") as f:
            f.write("# Store your secrets here\n")
            f.write('API_KEY = "your-api-key-here"\n')
        print("Created .streamlit/secrets.toml with API_KEY placeholder")
    else:
        print(".streamlit/secrets.toml already exists")

    # 3. Add .streamlit/ to .gitignore if it doesn't exist
    gitignore_content = ""
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            gitignore_content = f.read()

    if ".streamlit/" not in gitignore_content:
        with open(".gitignore", "a") as f:
            if gitignore_content and not gitignore_content.endswith("\n"):
                f.write("\n")
            f.write("# Streamlit secrets\n.streamlit/\n")
        print("Added .streamlit/ to .gitignore")
    else:
        print(".streamlit/ already in .gitignore")

    # 4. Create utils.py if it doesn't exist (with just a comment)
    if not os.path.exists("utils.py"):
        with open("utils.py", "w") as f:
            f.write("# Utility functions for the Streamlit application\n")
        print("Created utils.py with a comment")
    else:
        print("utils.py already exists")

    # 5. Create a notebook directory if it doesn't exist
    os.makedirs("notebook", exist_ok=True)
    print("Created notebook directory")

    # 6. Create a ipynb file inside notebook directory
    notebook_path = os.path.join("notebook", "api.ipynb")
    if not os.path.exists(notebook_path):
        with open(notebook_path, "w") as f:
            pass
        print(f"Created {notebook_path}")
    else:
        print(f"{notebook_path} already exists")

    print("\nMinimal Streamlit project setup completed successfully!")


if __name__ == "__main__":
    create_streamlit_minimal_structure()
