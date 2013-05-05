ColumnInline
============

Custom ColumnInline for Django admin. It renders each fieldset as a TR in a single TD

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
