ColumnInline
============

Custom ColumnInline for Django admin. It renders each fieldset as a TR in a single TD

Usage
-----

    from column_inline.admin import ColumnInline

    class MyInline(ColumnInline):
        ....
        (everything else as normal)

TODOs
-----

 * Add a bit of CSS to make it prettier.
