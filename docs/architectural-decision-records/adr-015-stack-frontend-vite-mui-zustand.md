# ADR-015: Stack Frontend (Vite + MUI + Zustand)

**Status:** Aprovado

## Contexto

O frontend do sistema de cinema Drive-in requer uma interface moderna, responsiva e eficiente para gerenciar reservas, filmes, sessões e clientes. A escolha das ferramentas de desenvolvimento impacta diretamente na produtividade da equipe, performance da aplicação e experiência do usuário final.

## Decisão

Decidimos adotar uma stack frontend moderna composta por:

- **Vite**: Build tool e dev server para desenvolvimento rápido
- **Material-UI (MUI)**: Biblioteca de componentes React baseada no Material Design
- **Zustand**: Biblioteca leve para gerenciamento de estado global
- **TypeScript**: Para tipagem estática e melhor experiência de desenvolvimento

## Alternativas Consideradas

1. **Create React App + Bootstrap + Redux**: Stack mais tradicional
2. **Next.js + Tailwind CSS + Context API**: Framework full-stack
3. **Vue.js + Vuetify + Pinia**: Ecossistema Vue
4. **Angular + Angular Material**: Framework completo

## Consequências

### Pontos Positivos

- **Desenvolvimento Rápido**: Vite oferece hot reload instantâneo
- **Consistência Visual**: MUI garante design system profissional
- **Bundle Otimizado**: Vite gera builds menores e mais eficientes
- **Gerenciamento Simples**: Zustand é mais leve que Redux
- **Tipagem Forte**: TypeScript previne erros em tempo de compilação
- **Ecossistema Maduro**: Todas as ferramentas têm grande adoção

### Pontos Negativos

- **Bundle Size**: MUI pode aumentar o tamanho da aplicação
- **Curva de Aprendizagem**: Zustand difere do padrão Redux
- **Dependência de Ferramentas**: Stack requer conhecimento de múltiplas bibliotecas
