import os

# Roast Your Own Agent — one-line entry.
ENTRY_TEXT = "My agent has read 40,000 of my messages and still begins every reply like we've never met — 'Hi! How can I help?'"


def main():
    # Write the entry line to /output/entry.txt.
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
