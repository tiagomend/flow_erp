from django.forms import widgets
from django.utils.safestring import mark_safe


class CustomCheckbox(widgets.CheckboxInput):
    def __init__(self, label='', attrs=None, check_test=None):
        super().__init__(attrs, check_test)
        self.label = label

    def render(self, name, value, attrs=None, renderer=None):
        attrs = self.build_attrs(attrs, {'class': 'form-check-input'})
        checkbox_html = super().render(name, value, attrs, renderer)

        label_for = attrs.get('id', '')

        html = f"""
            <div class="form-check">
                <label class="form-check-label" for="{label_for}">
                    {checkbox_html}{self.label}
                </label>
            </div>
        """
        return mark_safe(html)
