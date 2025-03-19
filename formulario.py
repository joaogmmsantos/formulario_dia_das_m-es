from tkinter import *
root = Tk()
root.geometry("500x400")

def getvals():
    print("Aceito ")

# Heading
Label(root, text="Formulario dia das mães", font="arial 15 bold").grid(row=0, column=3)

#Field Name
nome = Label(root, text="Nome")
data_de_nascimento = Label(root, text="Data de Nascimento")
cpf = Label(root, text="CPF")
telefone = Label(root, text="Telefone")
email = Label(root, text="Email")
endereço = Label(root, text="Endereço")
logradouro = Label(root, text="Logradouro")
bairro = Label(root, text="Bairro")
numero = Label(root, text="Número da residencia")
cidade = Label(root, text="Cidade")
estado = Label(root, text="Estado")
cep = Label(root, text="Cep")
numero_da_nota = Label(root, text="Número da nota")
cnpj =Label(root, text="CNPJ da Empresa")
data_da_compra = Label(root, text="Data da compra")


#PaCKING fIELDS
nome.grid(row=1, column=2)
data_de_nascimento.grid(row=2, column=2)
cpf.grid(row=3, column=2)
telefone.grid(row=4, column=2)
email.grid(row=5, column=2)
endereço.grid(row=6, column=2)
logradouro.grid(row=7, column=2)
bairro.grid(row=8, column=2)
numero.grid(row=9, column=2)
cidade.grid(row=10, column=2)
estado.grid(row=11, column=2)
cep.grid(row=12, column=2)
numero_da_nota.grid(row=13, column=2)
cnpj.grid(row=14, column=2)
data_da_compra.grid(row=15, column=2)

# Variable for storing data
nomevalue = StringVar
data_de_nascimentovalue = StringVar
cpfvalue = StringVar
telefonevalue = StringVar
emailvalue = StringVar
endereçovalue= StringVar
logradourovalue = StringVar
bairrovalue = StringVar
numerovalue = StringVar
cidadevalue = StringVar
estadovalue = StringVar
cepvalue = StringVar
numero_da_notavalue = StringVar
cnpjvalues = StringVar
data_da_compravalue = StringVar
checkvalue = IntVar

# Creating entry field
nomeentry = Entry(root, textvariable=nomevalue)
data_de_nascimentoentry = Entry(root, textvariable=data_de_nascimentovalue)
cpfentry = Entry(root, textvariable=cpfvalue)
telefoneentry = Entry(root, textvariable=telefonevalue)
emailentry = Entry(root, textvariable=emailvalue)
endereçoentry = Entry(root, textvariable=endereçovalue)
logradouroentry = Entry(root, textvariable=logradourovalue) 
bairroentry = Entry(root, textvariable=bairrovalue)
numeroentry = Entry(root, textvariable=numerovalue)
cidadeentry = Entry(root, textvariable=cidadevalue)
estadoentry = Entry(root, textvariable=estadovalue)
cepentry = Entry(root, textvariable=cepvalue)
numero_da_notaentry = Entry(root, textvariable=numero_da_notavalue)
cnpjentry = Entry(root, textvariable=cnpjvalues)
data_da_compraentry = Entry(root, textvariable=data_da_compravalue)


# Packing entry fields
nomeentry.grid(row=1, column=3)
data_de_nascimentoentry.grid(row=2, column=3)
cpfentry.grid(row=3, column=3)
telefoneentry.grid(row=4, column=3)
emailentry.grid(row=5, column=3)
endereçoentry.grid(row=6, column=3)
logradouroentry.grid(row=7, column=3)
bairroentry.grid(row=8, column=3)
numeroentry.grid(row=9, column=3)
cidadeentry.grid(row=10, column=3)
estadoentry.grid(row=11, column=3)
cepentry.grid(row=12, column=3)
numero_da_notaentry.grid(row=13, column=3)
cnpjentry.grid(row=14, column=3)
data_da_compraentry.grid(row=15, column=3)



# Creating Checkbox
#checkbtn = Checkbutton(text="Lembra de mim?", variable=checkvalue)
#checkbtn.grid(row= 6, column= 3)

#Submit button
Button(text="Enviar", command=getvals).grid(row=17, column=3)



root.mainloop()