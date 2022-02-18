(function ($) {
    $(document).ready(function () {
        const $level = $('#id_level').empty();
        $(document).on('change', '#id_rack', function () {
            const _this = $(this);
            $.ajax($ajax_getColletion, {
                method: "POST",
                data: {
                    app_label: 'custodia', model: 'level',
                    filters: `{'rack_id': '${_this.val()}'}`
                },
                success: function (response) {
                    $level.empty();
                    $level.append(`<option>---------</option>`)
                    $.each(response, function (i, level) {
                        $level.append(`
                            <option value="${level.id}">Nivel # ${level.code}</option>
                        `)
                    })
                }
            })
        })
    })
})(grp.jQuery)