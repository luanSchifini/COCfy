// Seleciona o elemento HTML com o ID "resultados-pesquisa" para exibir os resultados.
let section = document.getElementById("resultados-pesquisa");
let inputPesquisa = document.getElementById("campo-pesquisa");

// Função principal para realizar a pesquisa.
function pesquisar(pesquisa) {
  let resultados = "";
  let regex = new RegExp(`(${pesquisa})`, "gi");

  let dadosFiltrados = dados.filter(dado => {
    let nomeLower = dado.nome.toLowerCase();
    return nomeLower.includes(pesquisa);
  });

  if (dadosFiltrados.length === 0) {
    section.innerHTML = "<p>Nenhum resultado encontrado.</p>";
    return;
  }

  resultados = dadosFiltrados.map(dado => {
    let nomeDestacado = dado.nome.replace(regex, "<mark>$1</mark>");
    return `
      <div class="item-resultado">
        <h2>${nomeDestacado}</h2>
      </div>
    `;
  }).join('');

  section.innerHTML = resultados;
}

// Ouvinte de eventos para o campo de pesquisa.
inputPesquisa.addEventListener("input", function(event) {
  let pesquisa = event.target.value.toLowerCase();
  pesquisar(pesquisa);
});

// Ouvinte de eventos para o documento inteiro, limpando a seção de resultados ao clicar fora.
document.addEventListener("click", function(event) {
  if (!inputPesquisa.contains(event.target) && !section.contains(event.target)) {
    section.innerHTML = ""; 
  }
});

