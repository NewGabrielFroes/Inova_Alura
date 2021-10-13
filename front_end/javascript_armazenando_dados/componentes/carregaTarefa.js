import { Tarefa } from "./criaTarefa.js"

export const carregaTarefa = () => {
    const lista = document.querySelector('[data-list]')

    const tarrefasCadastradas = JSON.parse(localStorage.getItem('tarefas')) || []
    
    tarrefasCadastradas.forEach((tarefa) => {
        lista.appendChild(Tarefa(tarefa))
    })
}