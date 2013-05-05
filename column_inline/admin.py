from django.contrib.admin.options import InlineModelAdmin

# Custom Column Inline model admin 
class ColumnInline(InlineModelAdmin):
    template = 'admin/column_stacked.html'
    class Media:
            css = {
                "all": ("column_inline.css",)
            }

