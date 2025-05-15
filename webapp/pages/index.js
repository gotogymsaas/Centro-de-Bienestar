import { useTranslation } from 'next-i18next';

export default function Home() {
  const { t } = useTranslation('common');
  return (
    <main className="min-h-screen flex items-center justify-center">
      <h1 className="text-4xl font-bold">{t('welcome')}</h1>
    </main>
  );
}
