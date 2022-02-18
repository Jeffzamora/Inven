(function ($) {
    $(document).ready(function () {
        const $department = $('#id_department').empty();
        $(document).on('change', '#id_customer', function () {
            const _this = $(this);
            $.ajax($ajax_getColletion, {
                method: "POST",
                data: {
                    app_label: 'custodia', model: 'department',
                    filters: `{'customer_id': '${_this.val()}'}`
                },
                success: function (response) {
                    $department.empty();
                    $department.append(`<option>---------</option>`)
                    /*$.each(response, function (i, department) {
                        $department.append(`
                            <option value="${department.id}">${department.name}</option>
                        `)
                    })*/
                }
            })
        })
    })
})(grp.jQuery)