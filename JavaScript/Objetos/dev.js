

const devProfile = {
    name: "Felipe Oliver",
    apelido: "Felps",
    level: 25,
    techs: ["React", "ThreeJs", "JavaScript"],
    ativo: true,
    apresentar: function(){
        console.log(`Olá, eu sou ${this.name}, sou especialista em ${this.techs[0]}, e estou no nivel: ${this.level}`)
    }
}

console.log(devProfile.apresentar())

const devcompanheiro = devProfile;

console.log(devcompanheiro.name)
console.log(devProfile.name)
devcompanheiro.name = "Gabriel"

console.log(devcompanheiro.name)
console.log(devProfile.name)

let propriedade = "level"
console.log(devProfile[propriedade])

let relatorio = {
    "data de criação": "27-03-2026",
    "id-do-usuario": "abc-123"
}

console.log(relatorio["id-do-usuario"])
console.log(devProfile)
delete devProfile.ativo

console.log(devProfile.ativo)
console.log(devProfile)
console.log('=========================')

const devPro = {
    name: "Carlos Gonçalves",
    apelido: "carlinhos",
    level: 25,
    contato: {
        email: "carlos.unig7@gmail.com",
        telefone: "(18) 99160-9476",
        github: "carlos_uni7"
    },
    techStack: { 
        frontend: ["React", "ThreeJs", "JavaScript"],
        backend: ["Python", "Java", "Php"],
        mobile: false
    },
    ativo: true,
    apresentar: function(){
        console.log(`Olá, eu sou ${this.name}, sou especialista em ${this.techs[0]}, e estou no nivel: ${this.level}`)
    }
}