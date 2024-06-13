from django import forms
from .models import Usuario

class UsuarioForms(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Senha")
    email = forms.EmailField(label="E-mail")
    senha = forms.CharField(widget=forms.PasswordInput(), min_length=8, label="Senha")
    rg = forms.CharField(min_length=9, max_length=9, label="RG", help_text="Digite apenas os números do RG.")
    cnh = forms.CharField(min_length=11, max_length=11, label="CNH", help_text="Digite apenas os números da CNH.")

    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'senha', 'confirmar_senha', 'cpf', 'rg', 'cnh']
        widgets = {
            'senha': forms.PasswordInput(),
        }
        error_messages = {
            'senha': {
                'min_length': "A senha deve ter no mínimo 8 caracteres.",
            },
            'rg': {
                'min_length': "O RG deve ter 9 dígitos.",
                'max_length': "O RG deve ter 9 dígitos.",
            },
            'cnh': {
                'min_length': "A CNH deve ter 11 dígitos.",
                'max_length': "A CNH deve ter 11 dígitos.",
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")
        rg = cleaned_data.get("rg")
        cnh = cleaned_data.get("cnh")
        cpf = cleaned_data.get("cpf")

        if senha != confirmar_senha:
            raise forms.ValidationError("As senhas não conferem.")

        if not self.validar_rg(rg):
            raise forms.ValidationError("RG inválido.")

        if not self.validar_cnh(cnh):
            raise forms.ValidationError("CNH inválida.")

        if not self.validar_cpf(cpf):
            raise forms.ValidationError("CPF inválido.")

    def validar_rg(self, rg):
        # Exemplo simples: verificar se o RG tem exatamente 9 dígitos
        return len(rg) == 9 and rg.isdigit()

    def validar_cnh(self, cnh):
        # Exemplo simples: verificar se a CNH tem exatamente 11 dígitos
        return len(cnh) == 11 and cnh.isdigit()

    def validar_cpf(self, cpf):
        # Exemplo simples: verificar se o CPF tem exatamente 11 dígitos
        return len(cpf) == 11 and cpf.isdigit()
