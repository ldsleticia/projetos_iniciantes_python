def mostra_o_lugar():
    return lugar_selecionado()


def iniciar():
    print("A humanidade vive em cidades virtuais.")


# function printLugar() {
#   console.log(lugarSelecionado);
# }
#
# function iniciar() {
#   alert("A humanidade vive em cidades virtuais.");
#   escolheLugar();
# }
#
# function escolheLugar() {
#   let  lugarSelecionado = parseInt(
#     prompt(
#       "Vocês têm duas opções: entrar na matrix e tentar ajuda ou continuar a busca pelo portal no mundo real. Digite 0 para matrix ou 1 para mundo real"
#     )
#   );
#   printLugar();
#   if (lugarSelecionado === 0) {
#     matrix();
#   } else if (lugarSelecionado === 1) {
#     mundoReal();
#   } else {
#     alert("Erro. Recomece o jogo!!! ᕦ(ò_óˇ)ᕤ");
#   }
# }
#
# function matrix() {
#   let desconhecido = parseInt(
#     prompt("Confiar no desconhecido? Digite 0 para não ou 1 para sim")
#   );
#   if (desconhecido === 1) {
#     alert(
#       "Esse desconhecido era da CorpTow e tenta levar vocês a um laboratório da empresa. c(･o･)ɔ"
#     );
#     let lutar = parseInt(
#       prompt(
#         "Agora você tem duas opções, lutar ou tentar fugir. Digite 0 para lutar ou 1 para fugir"
#       )
#     );
#     if (lutar === 0) {
#       alert(
#         "Vocês mataram o funcionário da CorpTow e continuaram caminhando até chegar em uma ponte que parece ter passado despercebida por todos os habitantes e nela encontram a saída e voltam para o seu tempo └@(･◡･)@┐"
#       );
#     } else if(lutar === 1) {
#       alert(
#         "Os funcionários da CorpTow conseguiram te capturar e agora vocês passarão a eternidade no laboratório sendo cobaias da corporação (ಥ‸ಥ)"
#       );
#     } else {
#       alert("Erro. Recomece o jogo!!! ᕦ(ò_óˇ)ᕤ");
#     }
#   } else if (desconhecido === 0){
#     alert(
#       "Vocês decidem continuar procurando o caminho sozinhos e encontram após muitas horas de caminhada, uma ponte que parece ter passado despercebida por todos os habitantes e nela encontram a saída e voltam para o seu tempo └@(･◡･)@┐"
#     );
#   } else {
#     alert("Erro. Recomece o jogo!!! ᕦ(ò_óˇ)ᕤ");
#   }
# }
#
# function mundoReal() {
#   alert(
#     "Vocês encontram um vilarejo aparentemente abandonado. Vocês decidem inspecinar e ver o que encontram"
#   );
#   let inspecionar = parseInt(
#     prompt(
#       "Inspecionando a cidade, vocês encontram alguns humanos modificados. Tentam contato ou apenas passam pelo vilarejo? Digite 0 para contato ou 1 para passar direto"
#     )
#   );
#   if (inspecionar === 0) {
#     alert(
#       "Os humanos não entendem muito bem sua língua e levam vocês ao chefe do vilarejo. O chefe acha que vocês são uma ameaça e vocês ficam presos em uma das cadeias para sempre (ಥ‸ಥ)"
#     );
#   } else if(inspecionar === 1){
#     alert(
#       "Vocês tentam passar despercebidos e parece que funciona. Ao final do vilarejo vocês encontram uma árvore com uma porta estranha"
#     );
#     let arvoreEntrada = parseInt(
#       prompt(
#         "Vocês entram na árvore ou continuam andando? Digite 0 para entrar ou 1 para ignorar e continuar andando"
#       )
#     );
#     if (arvoreEntrada === 0) {
#       alert(
#         "Vocês abrem a porta, uma luz muito brilhante aparece ofuscando seus olhos e quando ela se vai, vocês estão em casa novamente └@(･◡･)@┐"
#       );
#     } else if (arvoreEntrada === 1){
#       alert(
#         "Vocês decidem continuar caminhando e a árvore some diante de vocês e em seu lugar aparece um pergaminho com a seguinte mensagem 'Eu era a sua saída, agora vocês estarão presos aqui para sempre (ಥ‸ಥ)'"
#       );
#     } else{
#       alert("Erro. Recomece o jogo!!! ᕦ(ò_óˇ)ᕤ");
#     }
#   } else{
#     alert("Erro. Recomece o jogo!!! ᕦ(ò_óˇ)ᕤ");
#   }
# }
