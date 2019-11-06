module.exports = {
    title: 'Ml blog',
    description: 'Todos os relatórios e afins sobre machine learning, deep learning e Visão computacional estarão aqui.',
    themeConfig: {
        displayAllHeaders: true,
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Relatorios', link: '/relatorio/' }
        ],
        sidebar: [
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
                    '/relatorio', 
                ]
            }
        ]
    },
}