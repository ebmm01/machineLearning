module.exports = {
    title: 'Estudo e Aplicação de Técnicas de Machine Learning',
    base: '/machineLearning/',
    description: 'Todos os relatórios e afins sobre machine learning, deep learning e Visão computacional estarão aqui.',
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Relatorios', link: '/relatorios/relatorio' },
            { text: 'Glossário', link: '/glossario/sobre_dl/'},
            { text: 'Artigos', link: '/artigos/'}
        ],
        sidebar: {
            '/relatorios/': [
                {
                    title: 'Machine Learning',
                    children: [
                        // These are pages we'll add later
                        'relatorioAP', 
                        'relatorioMl'
                    ]
                },
                {
                    title: 'Deep Learning',
                    children: [
                        //These are pages we'll add later
                       
                        'relatorio',
                        'relatorio_tfjs',
                    ]
                }
            ],
            '/glossario/': [
                {   
                    title: 'Conceitos & algoritmos',
                    children: [
                        'sobre_dl',
                        'algoritmos'
                    ]
                }
                
            ],
            '/artigos/': [
                ''
            ]
           
        }
    },
}