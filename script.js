$(document).ready(function () {
    // Відповідність категорії та CSS-класу
    const categoryClasses = {
        "Навчання": "category-study",
        "Робота": "category-work",
        "Особисте": "category-personal"
    };

    // Приклади елементів для кнопки "+ 3 випадкові"
    const samples = [
        { text: "Прочитати лекцію з jQuery", category: "Навчання" },
        { text: "Підготувати звіт до практичної", category: "Навчання" },
        { text: "Відповісти на листи", category: "Робота" },
        { text: "Оновити резюме", category: "Робота" },
        { text: "Піти на тренування", category: "Особисте" },
        { text: "Зателефонувати рідним", category: "Особисте" }
    ];

    const $list = $("#itemList");
    const $input = $("#itemText");
    const $error = $("#error");

    // Оновлення лічильників і повідомлення про порожній список
    function updateState() {
        const total = $list.children(".item").length;
        const done = $list.children(".item.done").length;
        $("#total").text(total);
        $("#done").text(done);
        $("#emptyMessage").toggle(total === 0);
    }

    // Створення нового елемента списку (текст вставляється через .text(), без ризику XSS)
    function createItem(text, category) {
        const $badge = $("<span>").addClass("badge").text(category);
        const $text = $("<span>").addClass("item-text").text(text);
        const $time = $("<span>").addClass("item-time").text(new Date().toLocaleTimeString("uk-UA"));
        const $delete = $("<button>")
            .attr({ type: "button", title: "Видалити" })
            .addClass("btn-delete")
            .text("✕");

        return $("<li>")
            .addClass("item " + categoryClasses[category])
            .append($badge, $text, $time, $delete)
            .hide();                          // спочатку прихований для анімації
    }

    // Додавання елемента: position = "end" (append) або "start" (prepend)
    function addItem(text, category, position) {
        const $item = createItem(text, category);
        if (position === "start") {
            $list.prepend($item);
        } else {
            $list.append($item);
        }
        $item.slideDown(300);
        updateState();
    }

    // Додавання з поля введення (з валідацією)
    function addFromForm(position) {
        const text = $input.val().trim();
        if (text.length < 2) {
            $error.text("Введіть текст елемента (щонайменше 2 символи)").fadeIn();
            $input.focus();
            return;
        }
        $error.fadeOut();
        addItem(text, $("#itemCategory").val(), position);
        $input.val("").focus();
    }

    // Подія відправки форми (Enter або кнопка) — додавання в кінець
    $("#addForm").on("submit", function (e) {
        e.preventDefault();
        addFromForm("end");
    });

    // Додавання на початок списку
    $("#addStart").click(function () {
        addFromForm("start");
    });

    // Додавання трьох випадкових елементів
    $("#addRandom").click(function () {
        for (let i = 0; i < 3; i++) {
            const sample = samples[Math.floor(Math.random() * samples.length)];
            addItem(sample.text, sample.category, "end");
        }
    });

    // Очищення списку
    $("#clearAll").click(function () {
        $list.children(".item").slideUp(300, function () {
            $(this).remove();
            updateState();
        });
    });

    // Делегування подій: працює і для елементів, доданих динамічно
    $list.on("click", ".item-text", function () {
        $(this).closest(".item").toggleClass("done");
        updateState();
    });

    $list.on("click", ".btn-delete", function () {
        $(this).closest(".item").slideUp(300, function () {
            $(this).remove();
            updateState();
        });
    });

    // Ховаємо повідомлення про помилку при введенні тексту
    $input.on("input", function () {
        $error.fadeOut();
    });

    // Ефект підсвічування полів при фокусі
    $("input, select").focus(function () {
        $(this).css("border-color", "#5b7bd5");
    }).blur(function () {
        $(this).css("border-color", "#3b5999");
    });

    updateState();
});
