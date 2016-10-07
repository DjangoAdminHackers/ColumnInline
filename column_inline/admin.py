from django.contrib.admin.options import InlineModelAdmin

 
class ColumnInline(InlineModelAdmin):
    
    template = 'admin/edit_inline/column_stacked.html'
    
    class Media:
        css = {"all": ("column_inline.css",)}


class CompactInline(InlineModelAdmin):
    
    template = 'admin/edit_inline/compact_stacked.html'
    
    class Media:
        css = {"all": ("compact_inline.css",)}
