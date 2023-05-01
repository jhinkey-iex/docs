> **DEPRECATED:** This repository is no longer the source for IEX Cloud Apperate documentation; the documentation source resides in the IEX Cloud Apperate product and is published at <https://iexcloud.io/documentation/>. Documentation requests or issues can be raised to [IEX Cloud Support](https://iexcloud.io/support/).

We write Markdown files that use an expansion syntax called [MyST](https://myst-parser.readthedocs.io/en/latest/intro.html) (Markedly Structured Text). Here are some helpful Markdown MyST articles.

- [CommonMark](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html) basic syntax.
- [Articles](https://pradyunsg.me/furo/reference/) that contain additional examples that include extensions we use via the Euro theme. **Important:** Selet the **Markdown (MyST)** tabs when you view the examples.

All of the articles are nested in the `source/` folder. The article/section hierarchy follows the `source/` folder's nested hierarchy of Markdown files (`.md`) and folders. The Markdown files, starting with `source/index.md` specify the hierarchy via [MyST style `{toc}` directives](https://coderefinery.github.io/sphinx-lesson/toctree/). 

Here is a representative sampling of repository files:

| File | Description |
| --- | --- |
| `source/administration/access-and-security.md` | Article called *Access and Security*. |
| `source/administration/access-and-security/` | Folder contains the above article’s image files. |
| `source/migrating-and-importing-data.md` | A section intro article (i.e., parent article) called *Migrating and Importing Data*. Its `{toc}` tree at the article top lists child articles. |
| `source/migrating-and-importing-data/` | Folder…<br> - Contains the parent article’s image files<br>- Contains the child articles and their image file folders |

## Related Topics

[Build instructions](./BUILD_INSTRUCTIONS.md)
