module.exports = {
    title: 'Estudo e Aplicação de Técnicas de Machine Learning',
    base: '/machineLearning/',
    description: 'Todos os relatórios e afins sobre machine learning, deep learning e Visão computacional estarão aqui.',
    themeConfig: {
        nav: [
            { text: 'Artigos', link: '/artigos/sobre'},
            { text: 'Glossário', link: '/glossario/funcoes/'},
            { text: 'Relatorios', link: '/relatorios/relatorio' },
        ],
        sidebar: {
            '/artigos/': [
                {
                    title: 'Artigos',
                    children: [
                        'sobre',
                        'ideia',
                        'artigo1',
                        'artigo2',
                        'artigo3',
                        'artigo4',
                        'artigo5',
                        'artigo6',
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
                        'funcoes',
                        'sobre_dl',
                        'algoritmos',
                    ]
                }
            ],
        }
    },
}