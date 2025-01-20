import flet as ft

def main(page: ft.Page):
    page.title = "Gerenciador de Notas"
    page.bgcolor = ft.Colors.WHITE

    def atualizar_tabela_notas(e):        
        for row in tabela.rows:
            if row.cells[0].content.value == materias.value:
                if tiponota.value == "aaa":
                    row.cells[1].content.value = notas.value
                elif tiponota.value == "aaaa":
                    row.cells[2].content.value = notas.value
                elif tiponota.value == "aaaaa":
                    row.cells[3].content.value = notas.value
                total = sum(int(row.cells[i].content.value) for i in range(1, 4))
                row.cells[4].content.value = str(total)
        page.update()

    def adicionar_materia(e):
        nova_materia = mat_add.value.strip()
        if nova_materia and nova_materia not in [row.cells[0].content.value for row in tabela.rows]:
            tabela.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(nova_materia, color=ft.Colors.PURPLE, weight=ft.FontWeight.BOLD)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
            ]))
            
            materias.content.controls.append(
                ft.Radio(value=nova_materia, label=nova_materia, fill_color=ft.Colors.PURPLE, label_style=ft.TextStyle(color=ft.Colors.BLACK))
            )
            mat_add.value = ""  
            page.update()


    notas = ft.TextField(
        label="Digite sua nota", 
        icon=ft.icons.NEWSPAPER_ROUNDED, 
        keyboard_type=ft.KeyboardType.NUMBER,  
        text_style=ft.TextStyle(color=ft.Colors.GREY),  
        label_style=ft.TextStyle(color=ft.Colors.BLACK),  
        border_color=ft.Colors.BLACK 
    )


    mat_add = ft.TextField(
        label='Digite uma matéria',
        icon=ft.icons.NEWSPAPER_ROUNDED, 
        text_style=ft.TextStyle(color=ft.Colors.GREY),
        label_style = ft.TextStyle(color=ft.Colors.BLACK),
        border_color=ft.Colors.BLACK
    )

    botao_add = ft.ElevatedButton(
        text="+", 
        on_click=adicionar_materia,
        style=ft.ButtonStyle(
            color=ft.Colors.BLACK,
            bgcolor=ft.Colors.BLUE,
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )


    materias = ft.RadioGroup(content=ft.Column(
        [
            ft.Radio(value="Matemática", label="Matemática", fill_color=ft.Colors.BLUE, label_style=ft.TextStyle(color=ft.Colors.BLACK)),
            ft.Radio(value="Português", label="Português", fill_color=ft.Colors.ORANGE, label_style=ft.TextStyle(color=ft.Colors.BLACK)),
            ft.Radio(value="Ciências", label="Ciências", fill_color=ft.Colors.GREEN, label_style=ft.TextStyle(color=ft.Colors.BLACK)),
        ],
        spacing=10, 
    ))


    tiponota = ft.RadioGroup(content=ft.Row(
        [
            ft.Radio(value="aaa", label="Nota 1", fill_color=ft.Colors.BLACK, label_style=ft.TextStyle(color=ft.Colors.BLACK)),
            ft.Radio(value="aaaa", label="Nota 2", fill_color=ft.Colors.BLACK, label_style=ft.TextStyle(color=ft.Colors.BLACK)),
            ft.Radio(value="aaaaa", label="Nota 3", fill_color=ft.Colors.BLACK, label_style=ft.TextStyle(color=ft.Colors.BLACK)),
        ],
        alignment=ft.MainAxisAlignment.CENTER, 
        spacing=15
    ))

  
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Matéria", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Nota 1", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD), numeric=True),
            ft.DataColumn(ft.Text("Nota 2", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD), numeric=True),
            ft.DataColumn(ft.Text("Nota 3", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD), numeric=True),
            ft.DataColumn(ft.Text("Nota Total", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD), numeric=True),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Matemática", color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Português", color=ft.Colors.ORANGE, weight=ft.FontWeight.BOLD)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Ciências", color=ft.Colors.GREEN, weight=ft.FontWeight.BOLD)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
                ft.DataCell(ft.Text("0", color=ft.Colors.BLACK)),
            ]),
        ],
    )


    layout_principal = ft.Row(
    [
      
        ft.Column(
            [
                ft.Text("Adicionar Matéria", size=18, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                mat_add,
                botao_add,
                ft.Text("Selecione uma matéria:", size=18, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                materias,
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,  
        ),

        ft.Column(
            [
                ft.Text("Atualizar Nota", size=18, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                notas,
                tiponota,
                ft.ElevatedButton("Atualizar Nota", on_click=atualizar_tabela_notas),
                tabela,
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.START,  
        ),
    ],
    spacing=50,  
    alignment=ft.MainAxisAlignment.CENTER, 
)


    page.add(layout_principal)

ft.app(main)