# container-diff-md-changelog

Generate a container image changelog file based on a JSON file coming from [container-diff](https://github.com/GoogleContainerTools/container-diff)

In other words: The expected JSON structure must match with a `container-diff` JSON output.

For more info about `container-diff` go to <https://github.com/GoogleContainerTools/container-diff>

## The command used in the tests

```bash
container-diff diff image:latest image:latest-1 --json --order --type=rpm --type=size --type=history > container_diff.json
```

For example:

```bash
container-diff diff fedora:38 fedora:37 --json --order --type=rpm --type=size --type=history > container_diff.json
```

## Usage

```bash
python container_diff_md_changelog.py container_diff.json CHANGELOG.md
```

One liner assuming `container-diff` is in the `$PATH`:

```bash
container-diff diff fedora:38 fedora:37 --json --order --type=rpm --type=size --type=history > container_diff.json && python container_diff_md_changelog.py container_diff.json CHANGELOG.md
```
