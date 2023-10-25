<!-- markdownlint-disable MD033 MD041 -->

<img
  align="right"
  alt="Logo of the Kaishi Starter Template"
  height="261"
  src="https://kura.pro/kaishi/images/logos/kaishi.svg"
  width="261"
  />

<!-- markdownlint-enable MD033 MD041 -->

# Kaishi.one 🌏

Welcome to [Kaishi.one](https://kaishi.one), a Starter Template for [Shokunin][1]!
This documentation will guide you through the process of getting up and running
with Kaishi in just a few minutes.

<!-- markdownlint-disable MD033 MD041 -->
<center>
<!-- markdownlint-enable MD033 MD041 -->

![Banner of the Kaishi Starter Template][banner]

<!-- markdownlint-disable MD033 MD041 -->
</center>
<!-- markdownlint-enable MD033 MD041 -->

## Installation

To use Kaishi, you'll need to install the Rust-based library called [Shokunin][1].
Follow the steps below to get started:

1. **Install the Rust toolchain**: Before installing Shokunin and Kaishi, make
   sure you have the Rust toolchain installed on your machine. You can find
   instructions for installing the Rust toolchain on the [Rust website][2].

2. **Install Shokunin**: Once you have the Rust toolchain installed, open your
   terminal and run the following command to install Shokunin:

```shell
cargo install ssg
```

Shokunin is the core library that powers Kaishi. It is a Rust-based static site
generator that can be used to generate a static website from a set of Markdown
files and HTML templates.

3. **Download the Kaishi Starter Template**: You can download the Kaishi Starter
   Template from the [Kaishi website](https://kaishi.one). Alternatively, you
   can download the Kaishi Starter Template directly from
   [GitHub](https://github.com/sebastienrousseau/kaishi.github.io)

## Usage 📖

Shokunin provides a simple command line interface (CLI) for managing and
building your website. Here are some of the most common commands:

- **Create a new site**: Use the following command to create a new site based on
  the Kaishi template:

```shell
cd kaishi/
ssg  --new=docs --content=content --template=template --output=output --serve=docs
```

Alternatively, you can use the shorthand version of the command:

```shell
cd kaishi/
ssg -n=docs -c=content -t=template -o=output --serve=docs
```

This command will create a new directory called `mysite` within the Kaishi project
directory. It will use the specified `content` directory for your site's content,
the `template` directory for the site's template files, and generate the output
files in the output directory. The --serve=public option allows you to serve the
generated website locally for testing and previewing.

Now you're ready to start building your website with Kaishi! Feel free to
customize the content, modify the template, and explore the features of Shokunin. 

Happy coding!

[banner]: https://kura.pro/kaishi/images/titles/title-kaishi.svg "Banner of the Kaishi Starter Template"
[0]: https://minifunctions.com/ "Mini Functions"
[1]: https://kaishi.one/ "Shokunin"
[2]: https://www.rust-lang.org/learn/get-started "Rust"
