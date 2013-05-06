ColumnInline
============

Custom ColumnInline for Django admin. It renders each fieldset as a TR in a single TD


A lot more compact horizontally than tabular and lot more company vertically than stacked. Especially if you have a mix of single line widgets and larger ones - such as textareas.

Normal Stacked Inline: ![Normal Stacked Inline](https://raw.github.com/DjangoAdminHackers/ColumnInline/master/docs/img/before.png)

Switch to Column Inline: ![Switch to Column Inline](https://raw.github.com/DjangoAdminHackers/ColumnInline/master/docs/img/after.png)

Usage
-----

Add 'column_inline' to INSTALLED_APPS so that Django knows where to find the templates.

The all you need is:

    from column_inline.admin import ColumnInline

    class MyInline(ColumnInline):
        ....
        (everything else as normal)

TODOs
-----

 * Add a bit of CSS to make it prettier.
