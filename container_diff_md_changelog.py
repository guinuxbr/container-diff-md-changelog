"""Generate a container image CHANGELOG.md file based on a JSON file.

Returns:
    string: A beatiful Markdown file 
"""
import json
import sys


def format_size(size_in_bytes: int) -> str:
    """Convert bytes to human-readable size
    Args:
        size_in_bytes (int): a size in bytes

    Returns:
        str: The size in a human-readable format
    """
    for unit in ["B", "KB", "MB", "GB"]:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} TB"


def build_markdown(json_path: str, markdown_path: str) -> str:
    """Receives the JSON path the builds the Markdown file.

    Args:
        json_path (str): The JSON file path
        markdown_path (str): The output Markdown file path.

    Returns:
        str: _description_
    """
    with open(json_path, "r", encoding="UTF-8") as json_file:
        jaon_data = json.load(json_file)

    changelog = "# CHANGELOG Generator\n"

    for entry in jaon_data:
        image_01 = entry["Image1"]
        image_02 = entry["Image2"]
        diff_type = entry["DiffType"]

        changelog += f"\n## {diff_type} Changes - {image_01} vs {image_02}\n\n"

        if diff_type == "History":
            additions = entry["Diff"]["Adds"]
            deletions = entry["Diff"]["Dels"]
            changelog += "### Added\n\n"
            for added_item in additions:
                changelog += f"- {added_item}\n"
            changelog += "\n### Deleted\n\n"
            for deleted_item in deletions:
                changelog += f"- {deleted_item}\n"

        elif diff_type == "RPM":
            packages_01 = entry["Diff"]["Packages1"]
            packages_02 = entry["Diff"]["Packages2"]
            package_diff = entry["Diff"]["InfoDiff"]

            changelog += "### Package Changes\n\n"

            changelog += "#### Added Packages\n\n"
            for package in packages_01:
                changelog += f"- **{package['Name']}**: {package['Version']} - Size: {format_size(package['Size'])}\n"

            changelog += "\n#### Removed Packages\n\n"
            for package in packages_02:
                changelog += f"- **{package['Name']}**: {package['Version']} - Size: {format_size(package['Size'])}\n"

            changelog += "\n#### Info Changes\n\n"
            changelog += f"| Package | Version (Size) - {image_01} | Version (Size) - {image_02} | Size Difference |\n"
            changelog += "| ------- | ------------------------ | ------------------------ | --------------- |\n"
            for info in package_diff:
                package_name = info["Package"]
                version_01 = info["Info1"]["Version"]
                size_01 = format_size(info["Info1"]["Size"])
                version_02 = info["Info2"]["Version"]
                size_02 = format_size(info["Info2"]["Size"])
                size_diff = format_size(info["Info1"]["Size"] - info["Info2"]["Size"])
                changelog += f"| {package_name} | {version_01} ({size_01}) | {version_02} ({size_02}) | {size_diff} |\n"

        elif diff_type == "Size":
            size_diff = entry["Diff"][0]
            _name = size_diff["Name"]
            size_01 = format_size(size_diff["Size1"])
            size_02 = format_size(size_diff["Size2"])
            size_diff_value = format_size(size_diff["Size1"] - size_diff["Size2"])
            changelog += "### Size Change\n\n"
            changelog += f"- {image_01} {size_01} -> {image_02} {size_02} (Size Difference: {size_diff_value})\n"

    # Write the changelog to a Markdown file
    with open(markdown_path, "w", encoding="UTF-8") as markdown_file:
        markdown_file.write(changelog)


if __name__ == "__main__":
    JSON_FILE_PATH = sys.argv[1]
    MARKDOWN_FILE_PATH = sys.argv[2]

    build_markdown(JSON_FILE_PATH, MARKDOWN_FILE_PATH)
