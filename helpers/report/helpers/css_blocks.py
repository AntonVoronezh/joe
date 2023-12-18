section = '''
<section class="section" id="%section_id%">
    <h3>%section_name%</h3>
    <div class="section-inner">
        %section_content%
    </div>
</section>
'''

yakor = '''
        <a href="#%section_id%" title="перейти к этой части">%section_name%</a>

'''

img = '''
        <div>
            <img src="%img%" width="200px">
        </div>
'''

card = f'''
 <div class="card">
        <h6 class="card-title">%title%</h6>
        <div class="card-text">%content%</div>
        
        <!--img-->
               
        <div class="modal" data-modal="%modal_id%">
            <span class="close js-modal-close">X</span>
            <p class="modal__title"><img src="%img%" width="100%"></p>
        </div>
        <a href="#" class="js-open-modal modal-link" data-modal="%modal_id%">Увеличить</a>
</div>
'''

h_1_title = '<h1 class="title">Проверка канала  %channel_name%  (%data%)</h1>'