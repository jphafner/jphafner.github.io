

Clone this repo and run to get everything

```
git checkout source
cd themes
git submodule update --init --recursive.
```

to update this, do this

```
git submodule update --remote --merge
```

$ cargo install --locked --git https://github.com/getzola/zola


https://catppuccin.com/


zola

fast static site generator with everything built-in

Usage: zola [OPTIONS] <COMMAND>

Commands:
  init        Create a new Zola project
  build       Deletes the output directory if there is one and builds the site
  serve       Serve the site. Rebuild and reload on change automatically
  check       Try to build the project without rendering it. Checks links
  completion  Generate shell completion
  help        Print this message or the help of the given subcommand(s)

Options:
  -r, --root <ROOT>      Directory to use as root of project [default: .]
  -c, --config <CONFIG>  Path to a config file other than zola.toml or config.toml in the root of project
  -h, --help             Print help
  -V, --version          Print version

License: EUPL-1.2 <https://eupl.eu>, MIT for code existing before 0.22



