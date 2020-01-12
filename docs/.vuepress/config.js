module.exports = {
    title: 'Estudo e Aplicação de Técnicas de Machine Learning',
    base: '/machineLearning/',
    description: 'Todos os relatórios e afins sobre machine learning, deep learning e Visão computacional estarão aqui.',
    themeConfig: {
        nav: [
            { text: 'Artigos', link: '/artigos/'},
            { text: 'Glossário', link: '/glossario/sobre_dl/'},
            { text: 'Relatorios', link: '/relatorios/relatorio' },
        ],
        sidebar: {
            '/artigos/': [
                {
                    title: 'Artigos',
                    children: [
                        'sobre',
                        'artigo1'
                    ]
                }
            ],
            '/relatorios/': [
                {
                    title: 'Machine Learning',
                    children: [
                        'relatorioAP', 
                        'relatorioMl'
                    ]
                },
                {
                    title: 'Deep Learning',
                    children: [
                        'relatorio',
                        'relatorio_tfjs',
                    ]
                }
            ],
            '/glossario/': [
                {   
                    title: 'Glossário',
                    children: [
                        'sobre_dl',
                        'algoritmos',
                        'funcoes'
                    ]
                }
            ],
        }
    },
}