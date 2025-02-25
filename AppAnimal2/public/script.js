async function carregarAnimais() {
  const response = await axios.get("http://127.0.0.1:8000/animais/");
  const animais = response.data;
  const lista = document.getElementById("lista-animais");
  lista.innerHTML = "";
  animais.forEach((animal) => {
    const item = document.createElement("li");
    item.innerText = animal.nome;
    lista.appendChild(item);
  });
}
function manipularFormulario() {
  const input_nome = document.getElementById("nome");
  const form_animal = document.getElementById("form-animal");
  form_animal.onsubmit = async (e) => {
    e.preventDefault();
    const nome_animal = input_nome.value;
    console.log("dados enviados", {
      nome_animal,
      idade: 3,
      sexo: "feminina",
      cor: "branca",
    });
    await axios.post("http://127.0.0.1:8000/animais", {
      nome: nome_animal,
      idade: 4,
      sexo: "feminina",
      cor: "branca",
    });
    carregarAnimais();
    alert("animal cadastrado... ");
  };
}
function app() {
  carregarAnimais();
  manipularFormulario();
}

app();
