## Atividade Prática 04

### Design Patterns (Padrões de Projeto) – Abstract Factory

### Questionário

**1. O que é o padrão de projeto Abstract Factory e qual é o seu objetivo principal?**
    <div><a style="color: cornflowerblue">Reposta:</a> É um padrão criacional que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.</div>

**2. Como o padrão Abstract Factory ajuda a promover o princípio de "programe para uma interface, não para uma implementação"?**
    <div><a style="color: cornflowerblue">Reposta:</a> Ele força o uso de interfaces ou classes abstratas para criar objetos, desacoplando o código da implementação concreta.</div>

**3. Quais são os componentes principais do padrão Abstract Factory? Explique cada um**
    <div><a style="color: cornflowerblue">Reposta:</a> - **Abstract Factory**: Interface que declara os métodos de criação. - **Concrete Factory**: Implementa a Abstract Factory para criar objetos concretos. - **Abstract Product**: Interface comum para os produtos. - **Concrete Product**: Implementação específica do produto. - **Client**: Usa a Abstract Factory para criar objetos sem saber suas classes concretas.</div>

**4. No exemplo da pizzaria, como o padrão Abstract Factory contribui para garantir consistência nos ingredientes utilizados?**
    <div><a style="color: cornflowerblue">Reposta:</a> As fábricas concretas garantem que as pizzas utilizem apenas ingredientes da mesma região ou tipo, mantendo a consistência.</div>

**5. Explique a diferença entre os padrões Abstract Factory e Factory Method**
    <div><a style="color: cornflowerblue">Reposta:</a> Abstract Factory cria famílias de objetos relacionados, enquanto Factory Method foca na criação de um único produto usando subclasses.</div>

**6. Quais são as vantagens do uso do padrão Abstract Factory em projetos de software?**
    <div><a style="color: cornflowerblue">Reposta:</a>Desacopla o código da implementação concreta, facilita a criação de famílias de objetos e promove a consistência entre objetos relacionados.</div>

**7. Como o padrão Abstract Factory pode ser aplicado para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas?**
    <div><a style="color: cornflowerblue">Reposta:</a> Através de fábricas concretas que implementam uma interface comum para criar produtos compatíveis.</div>

**8. Descreva uma situação do mundo real, diferente da pizzaria, onde o padrão Abstract Factory seria uma boa escolha**
    <div><a style="color: cornflowerblue">Reposta:</a> Sistemas de UI que precisam criar componentes (botões, janelas, menus) para diferentes plataformas, como Windows e macOS.</div>

**9. Quais são os possíveis desafios ou desvantagens do uso do padrão Abstract Factory em um sistema?**
    <div><a style="color: cornflowerblue">Reposta:</a> - Aumenta a complexidade do código. - Adiciona mais classes e interfaces, tornando a manutenção mais difícil.</div>

**10. Como o padrão Abstract Factory pode ser combinado com outros padrões de projeto, como o Singleton ou o Builder, para resolver problemas complexos de design?**
    <div><a style="color: cornflowerblue">Reposta:</a> Pode ser combinado com Singleton para garantir uma única instância da fábrica e com Builder para construir objetos complexos usando a fábrica abstrata.</div>
