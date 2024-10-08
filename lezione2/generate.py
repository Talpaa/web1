def genera_pag_html(n: int):

    pag11 = '''<div id="Pagina11" class="container text-center">
                 <div class="row">
                     <div class="col">
                           <img src="img/sito/logo_amazon.png" alt="Logo Amazon" width="100" height="100">
                           AMAZON
                      </div>
                  </div>
            </div>
            <br>'''
    
    pag12 = '''<div id="Pagina12" class="container text-center">
                    <div class="row">
                        <div class="col">
                            <a href="https://www.amazon.it/Regolabarba-lInnovativa-Regolabile-QP2734-30/dp/B0C815WY3Z?ref=dlx_deals_dg_dcl_B0C815WY3Z_dt_sl14_eb"><img src="img/prod/prod1.png" alt="Logo Amazon" width="400" height="350">
                            <br>Philips OneBlade 360 Face</a> 
                        </div>
                        <div class="col">
                            <a href="https://www.amazon.it/elettrico-rifinitore-confezione-QP440-50/dp/B0CVXSK4D3?ref=dlx_deals_dg_dcl_B0CVXSK4D3_dt_sl14_eb"><img src="img/prod/prod2.png" alt="Logo Amazon" width="400" height="350">
                            <br>Philips Genuine OneBlade 360 Lama di ricambio</a>
                        </div>
                        <div class="col">
                            <a href="https://www.amazon.it/TECLAST-Portatile-Notebook-12GB-Dimensione/dp/B0D12RN243?ref=dlx_deals_dg_dcl_B0D12RN243_dt_sl14_eb"><img src="img/prod/prod3.png" alt="Logo Amazon" width="400" height="350">
                            <br>TECLAST PC Portatile F16Plus Notebook 15.6" Full HD</a>
                        </div>
                    </div>
                </div>
                '''
    
    pag13 = '''<div id="Pagina13" class="container text-center">
                    <div class="row">
                        <div class="col">
                            <img src="img/sito/footer_amazon.png" alt="Logo Amazon" width="400" height="200">
                        </div>
                    </div>
                </div>'''
    
    pagina = pag11 + (pag12 * n) + pag13

    html_template = f'''<!DOCTYPE html>

                            <html lang="en">

                                <head>
                                    
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1">

                                    <title>HOME</title>

                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

                                    <link rel="stylesheet" type="text/css" href="stile.css"/>
                                    

                                </head>

                                <body>
                                    
                                    {pagina}
                                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                                    
                                </body>

                            </html>'''
    
    with open("./template.html", "w") as file:

        file.write(html_template)


if __name__ == "__main__":
    n = 5
    genera_pag_html(n)