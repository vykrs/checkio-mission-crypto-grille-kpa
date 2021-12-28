//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function cryptoGrilleKpaAnimation(tgt_node, data) {
            if (!data || !data.ext) {
                return
            }

            const input = data.in
            const result = data.ext.result
            const output = data.out

            /*----------------------------------------------*
             *
             * attr
             *
             *----------------------------------------------*/
            const attr = {
                inner_grid: {
                    'stroke-width': '1px',
                    'stroke': '#82D1F5',
                },
                grille: {
                    'stroke-width': '0px',
                    'stroke': '#294270',
                    'fill': '#82D1F5',
                    'opacity': 0.5,
                },
                letter: {
                    'font-family': 'sans-serif',
                    'font-weight': 'bold',
                    'stroke-width': 0,
                    'fill': '#294270',
                },
                description: {
                    'font-family': 'sans-serif',
                    'font-weight': 'bold',
                    'stroke-width': 0,
                    'fill': '#294270',
                    'font-size': '10px',
                },
            }

            /*----------------------------------------------*
             *
             * values
             *
             *----------------------------------------------*/
            const grid_size_px = 250
            const top_os = 10
            const bottom_os = 30
            const side_os = 10
            const width = 8
            const height = 8
            const unit = grid_size_px / width

            /*----------------------------------------------*
             *
             * paper
             *
             *----------------------------------------------*/
            const paper = Raphael(tgt_node,
                                    grid_size_px+side_os*2,
                                    grid_size_px+top_os+bottom_os, 0, 0)

            /*----------------------------------------------*
             *
             * draw grid
             *
             *----------------------------------------------*/
            for (let i = 0; i < 9; i += 1) {
                paper.path(['M', 0+side_os, i*unit+top_os, 'h', grid_size_px]).attr(attr.inner_grid)
                paper.path(['M', i*unit+side_os, 0+top_os, 'v', grid_size_px]).attr(attr.inner_grid)
            }

            /*----------------------------------------------*
             *
             * draw letters
             *
             *----------------------------------------------*/
            for (let i = 0; i < 8; i += 1) {
                for (let j = 0; j < 8; j += 1) {
                    paper.text(
                        j*unit+unit/2+side_os,
                        i*unit+unit/2+top_os,
                        input[1].slice(i*8+j, i*8+j+1)).attr(attr.letter).attr(
                            {'font-size': 20*Math.max(0.3, unit/50)})
                }
            }

            /*----------------------------------------------*
             *
             * draw grille
             *
             *----------------------------------------------*/
            const grille = paper.set()
            if (result) {
                for (let y = 0; y < 8; y += 1) {
                    for (let x = 0; x < 8; x += 1) {
                        if (output[y].slice(x, x+1) === '.') {
                            grille.push(paper.rect(
                                            x*unit+side_os,
                                            y*unit+top_os,
                                            unit, unit).attr(attr.grille))
                        }
                    }
                }
            }

            /*----------------------------------------------*
             *
             * rotate
             *
             *----------------------------------------------*/
            let degree = 0
            if (result) {
                tgt_node.onclick = function(){
                    degree += 90
                    grille.animate(
                        {transform: 'r' + String(degree) + ',' +
                        (grid_size_px/2+side_os)+',' +
                        (grid_size_px/2+top_os)},
                        1000, '<>'
                    )
                }
            }

            /*----------------------------------------------*
             *
             * description
             *
             *----------------------------------------------*/
            if (result) {
                paper.text(side_os+grid_size_px/2, top_os+bottom_os/2+grid_size_px,
                    'Click the grille to rotate 90 degrees').attr(attr.description)
            }

        }

        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'find_grille'
            },
            animation: function($expl, data){
                cryptoGrilleKpaAnimation(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
