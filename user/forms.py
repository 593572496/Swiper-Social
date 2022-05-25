from django import forms
from user.models import Profile


class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'location', 'min_distance', 'max_distance', 'min_age', 'max_age', 'dating_sex', 'vibration',
            'only_match',
            'auto_play'
        ]

    # 自己定义一些额外的验证，格式clean_ + 字段注意当验证到max_age时，会先验证clean_max_age是否通过，通过才会去验证后面的值（例如：使用clean_min_age时，后续手动清洗的数据中就不会有max_age）

    def clean_max_age(self):
        clean_data = super().clean()  # 手动清洗数据
        min_age = clean_data.get('min_age')
        max_age = clean_data.get('max_age')
        if min_age > max_age:
            raise forms.ValidationError('min_age>max_age')


