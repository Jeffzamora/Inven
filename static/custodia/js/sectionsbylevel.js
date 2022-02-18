(function ($) {
    $(document).ready(function () {
        const $section = $('#id_section').empty();
        $(document).on('change', '#id_level', function () {
            const _this = $(this);
            $.ajax($ajax_getColletion, {
                method: "POST",
                data: {
                    app_label: 'custodia', model: 'section',
                    filters: `{'level_id': '${_this.val()}'}`
                },
                success: function (response) {
                    $section.empty();
                    $section.append(`<option>---------</option>`)
                    $.each(response, function (i, seccion) {
                        $section.append(`
                            <option value="${seccion.id}">Sección # ${seccion.code}</option>
                        `)
                    })
                }
            })
        })
    })
})(grp.jQuery)