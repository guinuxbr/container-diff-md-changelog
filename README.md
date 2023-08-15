# container-diff-md-changelog

Generate a container image changelog file based on a JSON file coming from [container-diff](https://github.com/GoogleContainerTools/container-diff)

In other words: The expected JSON structure must match a `container-diff` JSON output.

For more info about `container-diff` go to <https://github.com/GoogleContainerTools/container-diff>

## Usage

```bash
python container_diff_md_changelog.py container_diff.json CHANGELOG.md
```

For example:

```bash
container-diff diff ubuntu:23.04 ubuntu:22.10 --json --order --type=apt --type=pip --type=node --type=size --type=history > container_diff.json
```

## The command used to generate `container_diff_example.json` and `CHANGELOG_example.md`

This one-liner assumes `container-diff` is in the `$PATH`:

```bash
container-diff diff ubuntu:23.04 ubuntu:22.10 --json --order --type=apt --type=pip --type=node --type=size --type=history > container_diff_example.json && python container_diff_md_changelog.py container_diff_example.json CHANGELOG_example.md
```
