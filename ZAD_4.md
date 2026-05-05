# Sposoby walki z botami
### Rejestracja wymagająca konta w zewnętrznym serwisie
To jest jedna z najlepszych metod przeciwdziałania botom w zakresie rejestracji kont. Aby zarejestrować się w naszej aplikacji, bot musi zarejestrować się również w danym serwisie. Dlatego gdy wymagamy np. konta Google do rejestracji, można powiedzieć, że nasza aplikacja dziedziczy po serwisie Google wszelką skuteczność w odsiewaniu botów przy rejestracji.

### Rate limiting
Praktycznie zawsze stosowane. W przeciwieństwie do globalnych limitów, rate limiting dość konkretnie celuje w boty, o ile limity ustawione są odpowiednio. To znaczy tak, aby pozwalać na zachowania typowe dla zwykłych użytkowników, ograniczając jednocześnie zachowania typowe dla botów. Np. ograniczenie dopuszczalnej liczby wyszukiwań do 30 co minutę wydaje mi się rozsądne dla wyszukiwarki internetowej. Zwykły użytkownik zazwyczaj nie przekroczy takiego limitu podczas normalnego użytkowania. 

### Ograniczenia równoległych połączeń oraz innych zachowań nietypowych
Bot może próbować otworzyć dużą liczbę połączeń naraz, by obezwładnić system. Takie ograniczenia to utrudniają. Mozemy np. ograniczać liczbę połączeń według adresu IP czy według tożsamości użytkownika.

Bot może również wysyłać zapytania nietypowe dla użytkowników. Załóżmy na przykład, że mamy aplikację z backendem oraz frontendem. Aplikacja jest skonfigurowana tak, by wysyłać konkretne headery oraz odpytywać backend co minutę.

Gdy ktoś odpytuje backend co sekundę lub wysyła niespodziewane headery, możemy być pewni, że nie korzysta z naszego frontnedu. Prawdopodobnie nie jest więc zwykłym użytkownikiem.

Logiczną decyzją będzie odrzucenie zapytań z tej strony.

### Przynęty (np. w formularzach)
Możemy ustawić w formularzu elementy takie jak niewidzialne pola. Użytkownik raczej ich nie wypełni, natomiast bot — być może tak. Wówczas możemy go zidentyfikować jako bota.

### Obserwacja zachowania
Na przykład ruchy myszki, prędkość reakcji, itp. Algorytmy uczenia maszynowego są wykorzystywane do klasyfikacji użytkowników poprzez tego typu znaczniki. O ile moja wiedza jest aktualna, to z tego korzysta checkbox "I'm not a robot", często spotykany na stronach korzystających z Cloudflare. Czasami wystarczy zaznaczyć checkbox, by przejść próbę. Prawdopodobnie samo zachowanie użytkownika na tym etapie jest ma wpływ na jego klasyfikacje.

### Publiczne bazy danych
Istnieją bazy danych udzielające informacji na temat adresów IP. Na przykład AbuseIPDB. Udostępnia ona informacje na temat wiarygodności różnych adresów IP, w szczególności takich, które mogą być powiązane z nadużyciami.

Przykładowo, moglibyśmy odpytywać bazę AbuseIPDB przy logowaniu oraz rejestracji użytkownika. Ktoś łączy się z naszą aplikacją. Nasz serwer przekazuje bazie AbuseIPDB IP przychodzącego połączenia. AbuseIPDB zwraca wynik odpowiadający prawdopodobieństwu, że wspomniany adres IP jest wykorzystywany w jakimś niecnym celu.

W tym momencie, my, czy raczej nasza aplikacja, może podjąć decyzję o dalszym postępowaniu.

### Odrzucanie zapytań na podstawie regionu
Nie jest to najmocniejsza forma obrony, gdyż nietrudno takie zabezpieczenie obejść (choćby przez VPN). Jednakże, sam fakt że atak może potrzebować dodatkowej warsty, to zawsze coś. Nie mówiąc o tym, że VPN i podobne rozwiązania też da się wykryć.

Załóżmy, że prowadzimy lokalny blog ściśle powiązany z miasteczkiem w Polsce. Być może nie ma konieczności, by użytkownicy z Chin lub Indii mieli do niego dostęp. Możemy więc rozważyć ograniczenie dostępu do Polski lub jakiegoś określonego regionu.

## Zastosowane zabezpieczenia
Niektóre ze wspomnienych zabezpieczeń zastosowałem w aplikacji z folderu [zad-3](./zad-3/) — konkretnie, są one skonfigurowane dla serwera nginx ([nginx.conf](./zad-3/nginx.conf)).



