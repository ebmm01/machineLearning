module.exports = {
    title: 'Estudo e Aplicação de Técnicas de Machine Learning',
    base: '/machineLearning/',
    description: 'Todos os relatórios e afins sobre machine learning, deep learning e Visão computacional estarão aqui.',
    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Relatorios', link: '/relatorio/' }
        ],
        sidebar: [
            '/sobre',
            {
                title: 'Machine Learning',
                sidebarDepth: 2,
                children: [
                    // These are pages we'll add later
                    '/relatorioAP', 
                    '/relatorioMl'
                ]
            },
            {
                title: 'Deep Learning',
                sidebarDepth: 2,
                children: [
                    // These are pages we'll add later
                    '/sobre_dl',
                    '/relatorio',
                    '/relatorio_tfjs',
                ]
            }
        ]
    },
}