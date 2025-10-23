If you want to change something in the core theme, you can copy the _sass folder and the assets/css/main.scss file to the website you are editing, and edit the theme with --livereload. When the result is satisfying, then you:

1) cut the folder and file and replace the ones in the core theme
2) upload the new version of the gem
3) upgrade the gem in the website

If you want to change something in the website, copy assets/css/main.scss from the core theme, and add a _sass folder

```
your-site/
└── _sass/
    ├── _theme-overrides.scss  # Override specific variables
    └── _custom-styles.scss    # Add new styles
```

```
// Load theme Sass (from gem/theme)
@import "theme-variables"; // This comes from the theme

// Your overrides
@import "theme-overrides"; // Override specific variables

// Load rest of theme
@import "theme-mixins";
@import "theme-layout";

// Your custom styles
@import "custom-styles";
```